"""DSC640 TSA complaint analysis and visualization pipeline.

Author: Anil Bammidi
Date: August 15, 2026

Inputs (provided with the assignment):
  - complaints-by-airport.csv
  - complaints-by-category.csv
  - complaints-by-subcategory.csv
  - iata-icao.csv

The script preserves the supplied complaint counts, separates records with and
without an airport code, joins airport codes to the supplied IATA/ICAO lookup,
and produces the six visuals used in the consolidated presentation.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import textwrap

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-tsa-assignment")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
from matplotlib import ticker as mtick
import numpy as np
import pandas as pd
import seaborn as sns


ROOT = Path(__file__).resolve().parents[2]
INPUT_DIR = ROOT / "upload"
OUTPUT_DIR = ROOT / "output" / "tsa_assignment"
CHART_DIR = OUTPUT_DIR / "charts"

AIRPORT_FILE = INPUT_DIR / "complaints-by-airport.csv"
CATEGORY_FILE = INPUT_DIR / "complaints-by-category.csv"
SUBCATEGORY_FILE = INPUT_DIR / "complaints-by-subcategory.csv"
IATA_FILE = INPUT_DIR / "iata-icao.csv"

BLUE = "#3D8DFF"
LIGHT_BLUE = "#A8DBF3"
ORANGE = "#E6863B"
DARK = "#111827"
MID = "#5B6472"
GRID = "#D9DEE7"
PALE = "#EEF3F8"
WHITE = "#FFFFFF"


STATE_ABBR = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
    "California": "CA", "Colorado": "CO", "Connecticut": "CT",
    "Delaware": "DE", "District of Columbia": "DC", "Florida": "FL",
    "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL",
    "Indiana": "IN", "Iowa": "IA", "Kansas": "KS", "Kentucky": "KY",
    "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN",
    "Mississippi": "MS", "Missouri": "MO", "Montana": "MT",
    "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH",
    "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
    "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH",
    "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA",
    "Rhode Island": "RI", "South Carolina": "SC", "South Dakota": "SD",
    "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT",
    "Virginia": "VA", "Washington": "WA", "West Virginia": "WV",
    "Wisconsin": "WI", "Wyoming": "WY",
}

# Approximate geography for a state tile map. This avoids adding an external
# boundary file while preserving a recognizable spatial layout.
STATE_TILE = {
    "WA": (0, 0), "MT": (2, 0), "ND": (3, 0), "MN": (4, 0),
    "MI": (6, 0), "VT": (9, 0), "NH": (10, 0), "ME": (11, 0),
    "OR": (0, 1), "ID": (1, 1), "WY": (2, 1), "SD": (3, 1),
    "WI": (5, 1), "NY": (8, 1), "MA": (10, 1), "RI": (11, 1),
    "NV": (1, 2), "NE": (3, 2), "IA": (4, 2), "IL": (5, 2),
    "IN": (6, 2), "OH": (7, 2), "PA": (8, 2), "NJ": (9, 2),
    "CT": (10, 2), "CA": (0, 3), "UT": (1, 3), "CO": (2, 3),
    "KS": (3, 3), "MO": (4, 3), "KY": (6, 3), "WV": (7, 3),
    "VA": (8, 3), "MD": (9, 3), "DE": (10, 3), "DC": (11, 3),
    "AZ": (1, 4), "NM": (2, 4), "OK": (3, 4), "AR": (4, 4),
    "TN": (6, 4), "NC": (8, 4), "TX": (3, 5), "LA": (4, 5),
    "MS": (5, 5), "AL": (6, 5), "GA": (7, 5), "SC": (8, 5),
    "AK": (0, 6), "HI": (1, 6), "FL": (8, 6),
}


def setup_style() -> None:
    sns.set_theme(style="whitegrid")
    plt.rcParams.update(
        {
            "figure.facecolor": WHITE,
            "axes.facecolor": WHITE,
            "axes.edgecolor": "#AAB2BF",
            "axes.labelcolor": DARK,
            "axes.titlecolor": DARK,
            "text.color": DARK,
            "xtick.color": MID,
            "ytick.color": MID,
            "font.family": "DejaVu Sans",
            "font.size": 12,
            "axes.titlesize": 20,
            "axes.titleweight": "bold",
        }
    )


def hide_spines(ax, names) -> None:
    """Hide selected axes spines across old and new Matplotlib versions."""
    for name in names:
        ax.spines[name].set_visible(False)


def load_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    airport = pd.read_csv(AIRPORT_FILE, dtype={"airport": "string"})
    category = pd.read_csv(CATEGORY_FILE, dtype={"airport": "string"})
    subcategory = pd.read_csv(SUBCATEGORY_FILE, dtype={"airport": "string"})
    iata = pd.read_csv(IATA_FILE, dtype={"iata": "string", "country_code": "string"})

    for frame in (airport, category, subcategory):
        frame["date"] = pd.to_datetime(frame["year_month"], format="%Y-%m")
        frame["scope"] = np.where(frame["airport"].notna(), "Airport-specific", "Not tied to an airport")
        frame["count"] = pd.to_numeric(frame["count"], errors="raise").astype(int)

    return airport, category, subcategory, iata


def save_figure(fig: plt.Figure, filename: str) -> None:
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(CHART_DIR / filename, dpi=220, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)


def chart_scope_trend(airport: pd.DataFrame) -> pd.DataFrame:
    data = (
        airport.groupby(["date", "scope"], as_index=False)["count"]
        .sum()
        .sort_values("date")
    )
    fig, ax = plt.subplots(figsize=(13.5, 7.2))
    palette = {"Airport-specific": BLUE, "Not tied to an airport": ORANGE}
    for scope in ["Airport-specific", "Not tied to an airport"]:
        part = data[data["scope"] == scope]
        # Convert pandas Series to NumPy arrays for compatibility with older
        # Matplotlib releases paired with newer pandas versions. Some older
        # Matplotlib versions internally use Series[:, None], which pandas no
        # longer supports.
        ax.plot(
            part["date"].to_numpy(),
            part["count"].to_numpy(),
            label=scope,
            color=palette[scope],
            linewidth=3,
        )
    ax.set_ylabel("Complaints per month")
    ax.set_xlabel("")
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
    ax.grid(axis="y", color=GRID, linewidth=0.8)
    ax.xaxis.grid(False)
    ax.legend(frameon=False, ncol=2, loc="upper left")
    hide_spines(ax, ("top", "right"))
    ax.text(0.0, -0.16, "Source: supplied complaints-by-airport.csv | January 2015-January 2024",
            transform=ax.transAxes, color=MID, fontsize=10)
    save_figure(fig, "01_scope_trend.png")
    return data


def build_state_totals(airport: pd.DataFrame, iata: pd.DataFrame) -> pd.DataFrame:
    allowed = {"US", "PR", "VI", "GU", "AS", "MP"}
    lookup = iata[iata["country_code"].isin(allowed)].copy()
    lookup = lookup.drop_duplicates("iata")
    airport_totals = (
        airport[airport["airport"].notna()]
        .groupby("airport", as_index=False)["count"].sum()
    )
    mapped = airport_totals.merge(
        lookup[["iata", "airport", "region_name", "country_code", "latitude", "longitude"]],
        left_on="airport", right_on="iata", how="left", suffixes=("_code", "_name")
    )
    mapped["state_abbr"] = mapped["region_name"].map(STATE_ABBR)
    state_totals = (
        mapped[mapped["state_abbr"].notna()]
        .groupby(["region_name", "state_abbr"], as_index=False)["count"].sum()
    )
    return mapped, state_totals


def chart_state_tile_map(state_totals: pd.DataFrame) -> pd.DataFrame:
    values = dict(zip(state_totals["state_abbr"], state_totals["count"]))
    bins = [0, 2500, 5000, 10000, 20000, np.inf]
    colors = ["#EDF5FB", "#C8E5F6", "#91C9EC", "#559EDD", "#1E5EA8"]
    labels = ["<2.5k", "2.5-5k", "5-10k", "10-20k", "20k+"]

    fig, ax = plt.subplots(figsize=(13.5, 7.2))
    ax.set_aspect("equal")
    for abbr, (x, y) in STATE_TILE.items():
        value = int(values.get(abbr, 0))
        idx = min(np.digitize([value], bins[1:-1], right=False)[0], len(colors) - 1)
        rect = plt.Rectangle((x, y), 0.92, 0.92, facecolor=colors[idx], edgecolor=WHITE, linewidth=2)
        ax.add_patch(rect)
        text_color = WHITE if idx >= 3 else DARK
        ax.text(x + 0.46, y + 0.36, abbr, ha="center", va="center", fontsize=12,
                fontweight="bold", color=text_color)
        ax.text(x + 0.46, y + 0.68, f"{value/1000:.1f}k" if value >= 1000 else f"{value}",
                ha="center", va="center", fontsize=8.5, color=text_color)

    ax.set_xlim(-0.2, 12.2)
    ax.set_ylim(7.2, -0.3)
    ax.axis("off")
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in colors]
    ax.legend(handles, labels, title="Total complaints", ncol=5, frameon=False,
              loc="lower center", bbox_to_anchor=(0.5, -0.02))
    ax.text(0.0, -0.09,
            "State tile map uses the supplied IATA/ICAO lookup; 50 states and DC shown. Counts are not adjusted for passenger volume.",
            transform=ax.transAxes, color=MID, fontsize=10)
    save_figure(fig, "02_state_tile_map.png")
    return state_totals


def chart_airport_boxplot(airport: pd.DataFrame) -> pd.DataFrame:
    coded = airport[airport["airport"].notna()].copy()
    top_codes = coded.groupby("airport")["count"].sum().nlargest(12).index.tolist()
    data = coded[coded["airport"].isin(top_codes)].copy()
    order = data.groupby("airport")["count"].median().sort_values().index.tolist()

    fig, ax = plt.subplots(figsize=(13.5, 7.2))
    sns.boxplot(data=data, y="airport", x="count", order=order, ax=ax, color=LIGHT_BLUE,
                width=0.62, linewidth=1.2, fliersize=3,
                flierprops={"markerfacecolor": ORANGE, "markeredgecolor": ORANGE, "alpha": 0.65})
    ax.set_xlabel("Monthly airport-specific complaints")
    ax.set_ylabel("")
    ax.xaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    ax.yaxis.grid(False)
    hide_spines(ax, ("top", "right", "left"))
    ax.text(0.0, -0.14,
            "Boxes show the middle 50% of monthly counts; orange points are statistical outliers, not confirmed operational failures.",
            transform=ax.transAxes, color=MID, fontsize=10)
    save_figure(fig, "03_airport_boxplot.png")
    return data[["airport", "date", "year_month", "count"]]


def chart_category_heatmap(category: pd.DataFrame) -> pd.DataFrame:
    complete = category[(category["date"].dt.year <= 2023)].copy()
    complete["year"] = complete["date"].dt.year
    top_categories = complete.groupby("clean_cat")["count"].sum().nlargest(9).index
    annual = complete.groupby(["year", "clean_cat"], as_index=False)["count"].sum()
    annual_total = complete.groupby("year")["count"].sum().rename("annual_total")
    annual = annual.merge(annual_total, on="year")
    annual["share"] = annual["count"] / annual["annual_total"]
    heat = annual[annual["clean_cat"].isin(top_categories)].pivot(
        index="clean_cat", columns="year", values="share"
    ).fillna(0)
    heat = heat.loc[top_categories]
    heat.index = ["\n".join(textwrap.wrap(x, 28)) for x in heat.index]

    fig, ax = plt.subplots(figsize=(13.5, 7.2))
    sns.heatmap(heat, cmap=sns.light_palette(BLUE, as_cmap=True), annot=True, fmt=".0%",
                linewidths=1, linecolor=WHITE, cbar_kws={"label": "Share of annual complaints"}, ax=ax)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.tick_params(axis="y", labelsize=10)
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_rotation(0)
    ax.text(0.0, -0.12,
            "Shares use all complaint categories. January 2024 is excluded because it is a partial year.",
            transform=ax.transAxes, color=MID, fontsize=10)
    save_figure(fig, "04_category_heatmap.png")
    return annual[annual["clean_cat"].isin(top_categories)].copy()


def chart_airport_categories(category: pd.DataFrame) -> pd.DataFrame:
    data = (
        category[category["airport"].notna()]
        .groupby("clean_cat", as_index=False)["count"].sum()
        .sort_values("count", ascending=False)
        .head(8)
        .sort_values("count")
    )
    total = category[category["airport"].notna()]["count"].sum()
    data["share"] = data["count"] / total
    labels = ["\n".join(textwrap.wrap(x, 34)) for x in data["clean_cat"]]

    fig, ax = plt.subplots(figsize=(13.5, 7.2))
    bars = ax.barh(
        labels,
        data["count"].to_numpy(),
        color=[BLUE if x == data["count"].max() else LIGHT_BLUE for x in data["count"]],
    )
    ax.set_xlabel("Complaints, 2015-January 2024")
    ax.set_ylabel("")
    ax.xaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    ax.yaxis.grid(False)
    hide_spines(ax, ("top", "right", "left"))
    for bar, share in zip(bars, data["share"]):
        ax.text(bar.get_width() + total * 0.008, bar.get_y() + bar.get_height()/2,
                f"{share:.0%}", va="center", fontsize=10, color=DARK)
    ax.text(0.0, -0.13,
            "Percent labels show each category's share of 583,495 airport-specific complaints.",
            transform=ax.transAxes, color=MID, fontsize=10)
    save_figure(fig, "05_airport_categories.png")
    return data


def chart_named_subcategories(subcategory: pd.DataFrame) -> pd.DataFrame:
    named = subcategory[(subcategory["airport"].notna()) & (subcategory["clean_subcat"].ne("*"))].copy()
    data = (
        named.groupby(["clean_cat", "clean_subcat"], as_index=False)["count"].sum()
        .sort_values("count", ascending=False)
        .head(10)
        .sort_values("count")
    )
    data["display"] = data["clean_subcat"].str.lstrip("*")
    labels = ["\n".join(textwrap.wrap(x, 34)) for x in data["display"]]

    fig, ax = plt.subplots(figsize=(13.5, 7.2))
    colors = [ORANGE if "TSO" in x or "Procedures" in x or "Lengthy" in x else BLUE for x in data["display"]]
    bars = ax.barh(labels, data["count"].to_numpy(), color=colors)
    ax.set_xlabel("Airport-specific complaints")
    ax.set_ylabel("")
    ax.xaxis.set_major_formatter(mtick.StrMethodFormatter("{x:,.0f}"))
    ax.grid(axis="x", color=GRID, linewidth=0.8)
    ax.yaxis.grid(False)
    hide_spines(ax, ("top", "right", "left"))
    for bar in bars:
        ax.text(bar.get_width() + 900, bar.get_y() + bar.get_height()/2,
                f"{int(bar.get_width()):,}", va="center", fontsize=10, color=DARK)
    ax.text(0.0, -0.13,
            "Rows with an unspecified clean subcategory ('*') are excluded from this ranking; no complaint records were deleted from the source files.",
            transform=ax.transAxes, color=MID, fontsize=10)
    save_figure(fig, "06_named_subcategories.png")
    return data


def add_processed_rows(rows: list[dict], visual_id: str, data: pd.DataFrame,
                       primary: str, value: str, secondary: str | None = None,
                       date_col: str | None = None, value_type: str = "count",
                       note: str = "") -> None:
    for _, record in data.iterrows():
        rows.append(
            {
                "visual_id": visual_id,
                "date": record[date_col].strftime("%Y-%m-%d") if date_col and pd.notna(record[date_col]) else "",
                "primary_group": str(record[primary]),
                "secondary_group": str(record[secondary]) if secondary else "",
                "value": float(record[value]),
                "value_type": value_type,
                "note": note,
            }
        )


def main() -> None:
    setup_style()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    airport, category, subcategory, iata = load_data()

    # Reconciliation: each complaint-level aggregation supplied by the source
    # must reproduce the same overall count.
    totals = {
        "airport_file": int(airport["count"].sum()),
        "category_file": int(category["count"].sum()),
        "subcategory_file": int(subcategory["count"].sum()),
    }
    if len(set(totals.values())) != 1:
        raise ValueError(f"Source totals do not reconcile: {totals}")

    scope_trend = chart_scope_trend(airport)
    mapped_airports, state_totals = build_state_totals(airport, iata)
    chart_state_tile_map(state_totals)
    airport_box = chart_airport_boxplot(airport)
    category_heat = chart_category_heatmap(category)
    airport_categories = chart_airport_categories(category)
    named_subcategories = chart_named_subcategories(subcategory)

    total = totals["airport_file"]
    airport_specific = int(airport.loc[airport["airport"].notna(), "count"].sum())
    not_tied = int(airport.loc[airport["airport"].isna(), "count"].sum())
    top_airports = (
        airport[airport["airport"].notna()].groupby("airport")["count"].sum().nlargest(10)
    )
    mapped_count = int(mapped_airports.loc[mapped_airports["region_name"].notna(), "count"].sum())
    coded_count = int(mapped_airports["count"].sum())
    peak_month = airport.groupby("year_month")["count"].sum().idxmax()
    peak_month_count = int(airport.groupby("year_month")["count"].sum().max())

    summary = {
        "date_range": [airport["year_month"].min(), airport["year_month"].max()],
        "total_complaints": total,
        "airport_specific": airport_specific,
        "airport_specific_share": airport_specific / total,
        "not_tied_to_airport": not_tied,
        "not_tied_share": not_tied / total,
        "peak_month": peak_month,
        "peak_month_count": peak_month_count,
        "top_airports": {k: int(v) for k, v in top_airports.items()},
        "iata_mapped_airport_complaints": mapped_count,
        "coded_airport_complaints": coded_count,
        "iata_mapping_coverage": mapped_count / coded_count,
        "source_reconciliation": totals,
        "cleaning_notes": [
            "No complaint counts were imputed or deleted.",
            "Missing airport codes were labeled 'Not tied to an airport' rather than assigned to a location.",
            "The supplied clean_cat and clean_subcat fields were used for grouping.",
            "Subcategory visual excludes only the unspecified clean_subcat='*' rows from its ranking.",
            "January 2024 is retained in totals and trends but excluded from annual-share heatmap as a partial year.",
            "Airport counts were joined to the supplied IATA/ICAO lookup by exact IATA code.",
        ],
    }
    (OUTPUT_DIR / "tsa_analysis_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")

    rows: list[dict] = []
    add_processed_rows(rows, "01_scope_trend", scope_trend, "scope", "count", date_col="date",
                       note="Monthly complaint totals by airport-code availability")
    add_processed_rows(rows, "02_state_tile_map", state_totals, "state_abbr", "count", secondary="region_name",
                       note="Airport-specific complaints joined to supplied IATA/ICAO lookup")
    add_processed_rows(rows, "03_airport_boxplot", airport_box, "airport", "count", date_col="date",
                       note="Monthly counts for 12 highest-volume airport codes")
    add_processed_rows(rows, "04_category_heatmap", category_heat, "clean_cat", "share", secondary="year",
                       value_type="share", note="Category share of annual complaints; 2015-2023")
    add_processed_rows(rows, "05_airport_categories", airport_categories, "clean_cat", "count",
                       value_type="count", note="Top airport-specific complaint categories")
    add_processed_rows(rows, "06_named_subcategories", named_subcategories, "display", "count", secondary="clean_cat",
                       note="Top named airport-specific subcategories; unspecified '*' excluded")
    pd.DataFrame(rows).to_csv(OUTPUT_DIR / "Anil_Bammidi_DSC640_TSA_Processed_Visual_Data.csv", index=False)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
