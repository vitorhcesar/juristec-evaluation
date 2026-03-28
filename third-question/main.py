import re

import pandas as pd

DADOS_EXTRAIDOS = {
    "id_processo": [101, 102, None, 104, 105],
    "valor_causa": ["R$ 1.500,00", "2000", "R$ 350,50", "5000.00", None],
    "status": ["Ativo", "encerrado", "ATIVO", "Arquivado", "Ativo"],
    "estado": ["SP", "RJ", "sp", "MG", "SP"],
}


def limpar_valor_causa(valor) -> float:
    """Converte strings monetárias mistas (BR / simples / None) em float."""
    if pd.isna(valor):
        return float("nan")
    s = str(valor).strip()
    if not s:
        return float("nan")
    s = re.sub(r"R\$\s*", "", s, flags=re.IGNORECASE).strip()
    if not s:
        return float("nan")
    # Formato brasileiro: separador de milhar '.' e decimal ','
    if "." in s and "," in s:
        s = s.replace(".", "").replace(",", ".")
    elif "," in s:
        s = s.replace(",", ".")
    try:
        number = float(s)
        if type(number) != float:
            return float(0)
        return number
    except ValueError:
        return float(0)


def preparar_dataframe(dados: dict) -> pd.DataFrame:
    df = pd.DataFrame(dados)
    df = df.dropna(subset=["id_processo"])
    df["id_processo"] = df["id_processo"].astype(int)
    df["status"] = df["status"].astype(str).str.strip().str.title()
    df["valor_causa"] = df["valor_causa"].apply(limpar_valor_causa)
    df["valor_causa"] = pd.to_numeric(df["valor_causa"], errors="coerce").fillna(0)
    return df


def main():
    df = preparar_dataframe(DADOS_EXTRAIDOS)
    print(df)

if __name__ == "__main__":
    main()
