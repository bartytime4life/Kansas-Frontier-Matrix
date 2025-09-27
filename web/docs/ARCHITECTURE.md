classDiagram
  direction LR

  class AppConfig {
    +version: string
    +title: string
    +subtitle: string
    +style: string
    +center: float[]        // e.g. [-98.3, 38.5]
    +zoom: number
    +time: TimeBounds
    +defaultYear: number
    +defaults: Defaults
    +groups: string[]
    +layers: Layer[]
  }

  class TimeBounds {
    +min: string           // YYYY-MM-DD
    +max: string           // YYYY-MM-DD
  }

  class Defaults {
    +minzoom: number
    +maxzoom: number
    +tileSize: number
    +visible: boolean
    +opacity: number
    +bounds: float[]       // [W,S,E,N]
    +time: TimeWindow
  }

  class Layer {
    +id: string
    +title: string
    +group: string
    +type: string          // raster|geojson|image
    +url: string           // for raster/image
    +path: string          // for geojson
    +opacity: number
    +visible: boolean
    +time: TimeWindow
    +paint: Paint          // geojson only
    +legend: LegendItem[]
    +attribution: string
    +minzoom: number
    +maxzoom: number
    +tileSize: number
  }

  class TimeWindow {
    +start: string         // YYYY-MM-DD or null
    +end: string           // YYYY-MM-DD or null
  }

  class Paint {
    +line: LinePaint
    +fill: FillPaint
    +circle: CirclePaint
  }

  class LinePaint {
    +line_color: string
    +line_width: number
    +line_opacity: number
  }

  class FillPaint {
    +fill_color: string
    +fill_opacity: number
    +fill_outline_color: string
  }

  class CirclePaint {
    +circle_color: string
    +circle_radius: number
    +circle_opacity: number
  }

  class LegendItem {
    +type: string          // line|fill|circle
    +label: string
    +color: string
    +width: number         // line only
    +outline: string       // fill only
    +radius: number        // circle only
  }

  AppConfig --> TimeBounds : time
  AppConfig --> Defaults   : defaults
  AppConfig --> Layer      : layers
  Defaults  --> TimeWindow : time
  Layer     --> TimeWindow : time
  Layer     --> Paint      : paint
  Layer     --> LegendItem : legend
  Paint     --> LinePaint
  Paint     --> FillPaint
  Paint     --> CirclePaint
