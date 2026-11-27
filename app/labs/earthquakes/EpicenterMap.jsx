'use client';

import { kansasPath, kansasProjection, useStoryCanvas } from '../../living-welcome/stories/story-kit.mjs';
import { CATALOG_BOUNDS } from './catalog-model.mjs';
import styles from './earthquake.module.css';

const FILL = ['#eeb477', '#a5d9dc'];
const [west, south, east, north] = CATALOG_BOUNDS;

export default function EpicenterMap({ comparison, layer, selected }) {
  const map = useStoryCanvas({
    draw(ctx, { w, h }) {
      ctx.clearRect(0, 0, w, h);
      const projection = kansasProjection(w, h, { padding: 16, bounds: { west, south, east, north } });
      const { x, y } = projection;
      ctx.fillStyle = '#142b3c';
      ctx.strokeStyle = '#7593a7';
      ctx.lineWidth = 1;
      ctx.setLineDash([4, 4]);
      ctx.strokeRect(x(west), y(north), x(east) - x(west), y(south) - y(north));
      ctx.setLineDash([]);
      const path = kansasPath(projection);
      ctx.fill(path);
      ctx.stroke(path);
      ctx.fillStyle = '#a1b7c4';
      ctx.font = '600 12px system-ui, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('KANSAS', x(-100.45), y(38.14));

      comparison.forEach(({ selected: events }, index) => {
        if (layer !== 'both' && Number(layer) !== index) return;
        ctx.fillStyle = FILL[index];
        ctx.globalAlpha = .47;
        for (const event of events) {
          const px = x(event.longitude), py = y(event.latitude);
          if (index === 0) {
            ctx.beginPath();
            ctx.arc(px, py, 2.6, 0, Math.PI * 2);
            ctx.fill();
          } else {
            ctx.fillRect(px - 2, py - 2, 4, 4);
          }
        }
      });
      ctx.globalAlpha = 1;

      if (selected) {
        ctx.beginPath();
        ctx.arc(x(selected.longitude), y(selected.latitude), 7, 0, Math.PI * 2);
        ctx.strokeStyle = '#fff9ed';
        ctx.lineWidth = 2;
        ctx.stroke();
      }
    },
    deps: [comparison, layer, selected],
  });

  return <canvas ref={map} role="img" className={styles.canvas}
    aria-label="Historical earthquake epicenters in the USGS search box around Kansas. The event records below list locations and let you highlight a point." />;
}
