import React from 'react';

type Props = {
  title: string;
  value: string | number;
  subtitle?: string;
};

export default function KpiCard({ title, value, subtitle }: Props) {
  return (
    <div className="kpi-card">
      <h3>{title}</h3>
      <strong>{value}</strong>
      {subtitle && <span>{subtitle}</span>}
    </div>
  );
}
