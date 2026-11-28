'use client';

import { kansasPath, kansasProjection, useStoryCanvas } from '../../living-welcome/stories/story-kit.mjs';
import { MAP_BOUNDS } from './season-model.mjs';
import styles from './tornado-season.module.css';

export default function SeasonMap({ coverage, layer }) {
  const map = useStoryCanvas({
    draw(ctx, { w, h }) {
      ctx.clearRect(0, 0, w, h);
      const projection = kansasProjection(w, h, { padding: 14, bounds: MAP_BOUNDS });
      const { x, y } = projection;
      const outline = kansasPath(projection);
      ctx.fillStyle = '#192d32';
      ctx.strokeStyle = '#789398';
      ctx.lineWidth = 1;
      ctx.fill(outline);
      ctx.stroke(outline);
      ctx.fillStyle = '#b5cacc';
      ctx.font = '600 12px system-ui, sans-serif';
      ctx.fillText('KANSAS', x(-101.45), y(37.29));

      if (layer === 'lines') {
        ctx.strokeStyle = '#ffbd81';
        ctx.globalAlpha = .56;
        ctx.lineWidth = 1.35;
        ctx.beginPath();
        for (const row of coverage.paths) {
          const [start, end] = row.geometry.coordinates;
          ctx.moveTo(x(start[0]), y(start[1]));
          ctx.lineTo(x(end[0]), y(end[1]));
        }
        ctx.stroke();
      } else {
        ctx.fillStyle = '#8ad5d4';
        ctx.globalAlpha = .56;
        for (const row of coverage.starts) ctx.fillRect(x(row.longitude) - 1.5, y(row.latitude) - 1.5, 3, 3);
      }
      ctx.globalAlpha = 1;
    },
    deps: [coverage, layer],
  });
  return <canvas ref={map} className={styles.canvas} role="img" aria-label={layer === 'lines'
    ? 'Straight segments between reported tornado endpoints. The selected source rows are listed below.'
    : 'Reported tornado start points in the Kansas map frame. The selected source rows are listed below.'}/>;
}
