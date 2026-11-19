'use client';

import { useStoryCanvas } from '../../living-welcome/stories/story-kit.mjs';
import styles from './river-flow.module.css';

const COLORS = ['#70d5db', '#f4c577'];
const tickText = new Intl.NumberFormat('en-US', { notation: 'compact', maximumFractionDigits: 1 });

function linearAxis(maximum) {
  const target = maximum / 4;
  const power = 10 ** Math.floor(Math.log10(target));
  const step = ([1, 2, 5, 10].find(value => value * power >= target) || 10) * power;
  const count = Math.ceil(maximum / step);
  return Array.from({ length: count + 1 }, (_, index) => step * index);
}

export function FlowChart({ curves, count, frequency, readings, scale }) {
  const ref = useStoryCanvas({
    draw(ctx, { w, h }) {
      ctx.clearRect(0, 0, w, h);
      const left = 49, right = w - 24, top = 18, bottom = h - 36;
      const maxFlow = Math.max(curves[0][0].value, curves[1][0].value, 1);
      const linear = scale === 'linear';
      const ticks = linear ? linearAxis(maxFlow) : [0, 1, 10, 100, 1000, 10_000, 100_000].filter(tick => tick <= maxFlow);
      const max = linear ? ticks.at(-1) : maxFlow;
      const height = linear ? value => value : Math.log1p;
      const x = percent => left + percent / 100 * (right - left);
      const y = value => bottom - height(value) / height(max) * (bottom - top);

      ctx.font = '12px system-ui, sans-serif';
      ctx.fillStyle = '#c7dce0';
      ctx.strokeStyle = '#345361';
      ctx.lineWidth = 1;
      ctx.textBaseline = 'middle';
      ctx.textAlign = 'right';
      for (const tick of ticks) {
        ctx.beginPath();
        ctx.moveTo(left, y(tick));
        ctx.lineTo(right, y(tick));
        ctx.stroke();
        ctx.fillText(tickText.format(tick), left - 8, y(tick));
      }

      ctx.textAlign = 'center';
      for (const tick of w < 370 ? [0, 25, 50, 75, 100] : [0, 20, 40, 60, 80, 100]) {
        ctx.fillText(`${tick}%`, x(tick), bottom + 18);
      }
      ctx.strokeStyle = '#d1e3e8';
      ctx.setLineDash([2, 4]);
      ctx.beginPath();
      ctx.moveTo(x(frequency), top);
      ctx.lineTo(x(frequency), bottom);
      ctx.stroke();

      curves.forEach((curve, index) => {
        ctx.strokeStyle = COLORS[index];
        ctx.lineWidth = 2.5;
        ctx.setLineDash(index ? [6, 4] : []);
        ctx.beginPath();
        ctx.moveTo(left, y(curve[0].value));
        curve.forEach((point, step) => {
          if (step) ctx.lineTo(x(curve[step - 1].count / count * 100), y(point.value));
          ctx.lineTo(x(point.count / count * 100), y(point.value));
        });
        ctx.stroke();
      });
      readings.forEach((point, index) => {
        ctx.fillStyle = COLORS[index];
        ctx.strokeStyle = '#09232e';
        ctx.setLineDash([]);
        ctx.lineWidth = 1.5;
        ctx.beginPath();
        ctx.arc(x(frequency), y(point.value), 4.5, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();
      });
    },
    deps: [curves, count, frequency, readings, scale],
  });
  return <canvas ref={ref} className={styles.canvas} role="img"
    aria-label="Flow-duration curves. Daily mean flow falls from rare high values on the left to common low values on the right. The selected values are listed below."/>;
}
