from pathlib import Path
import pandas as pd
import seaborn as sns
from fpdf import FPDF

import matplotlib.pyplot as plt


BASE = Path(__file__).resolve().parent
ASSETS = BASE / "assets"
OUTPUT = BASE / "output"


def ensure_dirs():
    ASSETS.mkdir(exist_ok=True)
    OUTPUT.mkdir(exist_ok=True)


def save_hist_log(df: pd.DataFrame, col: str, filename: str):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.histplot(data=df, x=col, ax=ax)
    ax.set_xscale("log")
    ax.set_title(f"Distribución real de {col} (escala log)")
    ax.set_xlabel(col)
    ax.set_ylabel("Frecuencia")
    sns.despine()
    path = ASSETS / filename
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return path


def save_count_ordered(df: pd.DataFrame, col: str, filename: str):
    order = df[col].value_counts().index
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.countplot(data=df, x=col, order=order, ax=ax)
    ax.set_title(f"{col} ordenado por volumen (historia, no alfabeto)")
    ax.set_xlabel(col)
    ax.set_ylabel("Cantidad")
    sns.despine()
    path = ASSETS / filename
    fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return path


def build_pdf(title: str, img_path: Path, narrative: str, out_name: str = "reporte_movilidad.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, title, ln=True, align="C")
    pdf.ln(4)

    pdf.image(str(img_path), w=190)
    pdf.ln(6)

    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 8, narrative)

    out_path = OUTPUT / out_name
    pdf.output(str(out_path))
    return out_path


def main():
    ensure_dirs()

    df = pd.read_csv("train.csv")

    img = save_hist_log(df, col="trip_duration", filename="hist_trip_duration_log.png")

    total = df.shape[0]
    narrative = f"Analizamos {total:,} registros. El histograma en escala log revela la concentración de valores bajos y la presencia de extremos."

    pdf_path = build_pdf("Reporte de Movilidad", img, narrative)
    print(f"[OK] PDF generado: {pdf_path}")


if __name__ == "__main__":
    main()