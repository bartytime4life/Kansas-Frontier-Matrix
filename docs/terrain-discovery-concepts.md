# Terrain & elevation: Kansas applications of OpenAI to Z concepts

Researched2026-11-24. This is a source-backed design adaptation, not a competition submission or a claim that Amazon-trained classifiers transfer to Kansas. No paid model calls, hosted cloud processing, new subscription, or Earth Engine activation is part of this implementation.

The owner's Kaggle Data page rendered no readable text in the web reader. Its linked official starter pack and checkpoints were read. The winners list identifies Black Bean first, GlyphTrack second, and Archaios fourth. The organizers emphasize converging spatial measurements, multiple public sources and reproducibility. Archaios describes DTM/DSM, slope, hillshade/local relief and comparison with imagery. GlyphTrack describes separate terrain signals and contextual evidence. These are entrant claims and design references, not independent validation of any Kansas detector.

## Implement in the current solid-terrain iteration

1. Three geographic solid-cell layers: Ground, Surface and Canopy height. Inspect a column and see its source value, coverage and origin. Current Kansas viewport replaces fixed example navigation.
2. Reveal landforms: height color, Horn3x3 slope, and7x7 local-relief residual on the measured Ground geometry. A near-flat broad view can hide local forms; linked analytic colors explain what the output grid resolves. Coarse statewide samples cannot reveal metre-scale features. Null support remains missing.
3. Reproducible terrain study: export the validated provider Ground grid, request key, source digest, retrieval metadata, output spacing and fixed analytic recipe. Other KFM science tools can consume the same typed inputs. A screenshot is not a substitute for the data and method.

## Kansas-specific next capabilities, not implemented claims

| Capability | Kansas question | Evidence/method needed |
|---|---|---|
| Linked terrain/imagery/history comparison | Does a linear embankment align with a documented rail grade or historical map? | Same camera and verified map registration; dates and spatial resolution for each layer; public archival reference. |
| Survey-aware before/after | Did a channel, quarry edge or bank change? | Registered elevations in comparable vertical datums and acquisition dates; common resolution; error propagation before interpreting a difference. |
| Cross-section and slope profiles | How do terrace heights, valley sides and drainage divide slopes vary along this line? | Unscaled supported elevations, ground distances, visible gaps; sample spacing and datum in export. |
| Multiscale terrain comparison | Is a pattern local roughness or a regional slope? | Labelled physical window sizes, sufficient source resolution, comparisons retaining original heights. |
| Reviewed landform leads | Which shapes merit further historical or field research? | Independent Kansas evidence and expert review; assess modern agriculture, roads and natural geology as alternative explanations. A terrain anomaly is not a cultural attribution, age or calibrated probability. |
| Reusable study annotations | Can someone reproduce and critique an interpretation? | Source IDs/hashes, data acquisition/retrieval distinction, measurements, method parameters, observation versus interpretation, and governed publication. |

Do not transplant Amazon soil/vegetation priors, reported confidence percentages or proxy classifiers to Kansas. The current no-added-cost pathway is free public USGS source data plus the existing dev14TB storage, local scientific Python and browser GPU. Keep the historical NEON/Konza example outside the primary Terrain card.

## Sources

- Owner links: https://www.kaggle.com/competitions/openai-to-z-challenge/data and https://www.kaggle.com/competitions/openai-to-z-challenge/hackathon-winners
- Official organizer: https://openai.com/openai-to-z-challenge/
- Official starter pack: https://cdn.openai.com/pdf/a9455c3b-c6e1-49cf-a5cc-c40ed07c0b9f/starter-pack-openai-to-z-challenge.pdf
- Official checkpoints: https://cdn.openai.com/pdf/a9455c3b-c6e1-49cf-a5cc-c40ed07c0b9f/checkpoints-openai-to-z-challenge.pdf
- Entrant method: https://www.kaggle.com/competitions/openai-to-z-challenge/writeups/archaios-explore-hidden-world-with-open-ai
- Authors' method PDF: https://storage.googleapis.com/kaggle-forum-message-attachments/3235107/22977/GlyphTrack_Detection_of_Anomalies_Under_Canopy.pdf
- Independent implementation definitions: https://gdal.org/en/stable/programs/gdaldem.html and https://proj.org/en/stable/operations/projections/webmerc.html
