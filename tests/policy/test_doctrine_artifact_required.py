from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = {
    "KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf",
    "Master_MapLibre_Components-Functions-Features.pdf",
    "Kansas_Frontier_Matrix_Definitive_Greenfield_Building_Plan_v1_1.pdf",
}

def test_required_doctrine_filenames_declared_in_registry():
    text = (ROOT / "control_plane" / "document_registry_doctrine_required.yaml").read_text(encoding="utf-8")
    files = {
        line.split(":", 1)[1].strip()
        for line in text.splitlines()
        if "filename:" in line
    }
    assert REQUIRED.issubset(files)
