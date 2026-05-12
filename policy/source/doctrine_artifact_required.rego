package kfm.doctrine_artifact_required

default deny := []

required := {
  "KFM_Pass_18_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf",
  "Master_MapLibre_Components-Functions-Features.pdf",
  "Kansas_Frontier_Matrix_Definitive_Greenfield_Building_Plan_v1_1.pdf"
}

deny contains reason if {
  some f in required
  not input.present[f]
  reason := sprintf("missing_required_doctrine_artifact:%s", [f])
}
