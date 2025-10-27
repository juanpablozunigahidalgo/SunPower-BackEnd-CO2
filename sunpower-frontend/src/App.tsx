import { useEffect, useState } from "react";
import { getNetEmissions } from "./api";

type NetResponse = {
  gross_emissions_kg: number;
  compensated_kg: number;
  net_emissions_kg: number;
  by_category: Record<string, number>;
};

function CardRow(props: { label: string; value: string; highlight?: boolean }) {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        marginBottom: ".5rem",
        fontSize: props.highlight ? "1.1rem" : ".9rem",
        fontWeight: props.highlight ? 600 : 400,
        color: props.highlight ? "#4ade80" : "white",
      }}
    >
      <span style={{ color: props.highlight ? "#fff" : "#94a3b8" }}>
        {props.label}
      </span>
      <span>{props.value}</span>
    </div>
  );
}

function App() {
  const [data, setData] = useState<NetResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  // On load, ask the backend for company 1 in 2025
  useEffect(() => {
    getNetEmissions(1, "2025-01-01", "2025-12-31")
      .then(setData)
      .catch((err) => {
        console.error(err);
        setError(
          "Could not load data. Did you create company 1, activities, solar project, and allocation in the backend?"
        );
      });
  }, []);

  return (
    <main
      style={{
        fontFamily:
          "system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif",
        background: "#0f172a",
        color: "white",
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        padding: "2rem",
      }}
    >
      <div
        style={{
          background: "#1e293b",
          borderRadius: "1rem",
          boxShadow: "0 30px 60px rgba(0,0,0,0.6)",
          padding: "2rem",
          width: "100%",
          maxWidth: "480px",
        }}
      >
        {/* Header */}
        <h1
          style={{
            fontSize: "1.25rem",
            fontWeight: 600,
            marginBottom: "0.5rem",
            color: "white",
          }}
        >
          SunPowerScope Dashboard
        </h1>

        <p
          style={{
            fontSize: "0.85rem",
            color: "#94a3b8",
            marginBottom: "2rem",
          }}
        >
          Company ID: 1 • Period: 2025
        </p>

        {/* Error state */}
        {error && (
          <div
            style={{
              backgroundColor: "#7f1d1d",
              color: "#fecaca",
              borderRadius: ".5rem",
              padding: ".75rem 1rem",
              fontSize: ".8rem",
              marginBottom: "1rem",
            }}
          >
            {error}
          </div>
        )}

        {/* Loading state */}
        {!data && !error && <div>Loading sustainability data…</div>}

        {/* Data view */}
        {data && (
          <>
            {/* Summary block */}
            <section style={{ marginBottom: "1.5rem" }}>
              <CardRow
                label="Gross emissions"
                value={`${data.gross_emissions_kg.toFixed(2)} kg CO₂e`}
              />

              <CardRow
                label="Solar compensation"
                value={`- ${data.compensated_kg.toFixed(2)} kg CO₂e`}
              />

              <div
                style={{
                  borderTop: "1px solid #334155",
                  marginTop: "1rem",
                  paddingTop: "1rem",
                }}
              >
                <CardRow
                  label="Net emissions"
                  value={`${data.net_emissions_kg.toFixed(2)} kg CO₂e`}
                  highlight
                />
              </div>
            </section>

            {/* Breakdown */}
            <section>
              <h2
                style={{
                  fontSize: "0.9rem",
                  color: "#94a3b8",
                  marginBottom: ".5rem",
                }}
              >
                Breakdown by category
              </h2>

              <div
                style={{
                  background: "#0f172a",
                  borderRadius: ".5rem",
                  padding: "1rem",
                }}
              >
                {Object.entries(data.by_category).map(([cat, val]) => (
                  <div
                    key={cat}
                    style={{
                      display: "flex",
                      justifyContent: "space-between",
                      fontSize: ".9rem",
                      paddingBottom: ".5rem",
                      borderBottom: "1px solid #1e293b",
                      marginBottom: ".5rem",
                      color: "white",
                    }}
                  >
                    <span style={{ color: "#fff" }}>{cat}</span>
                    <span style={{ color: "#94a3b8" }}>
                      {val.toFixed(2)} kg
                    </span>
                  </div>
                ))}

                {Object.keys(data.by_category).length === 0 && (
                  <div
                    style={{
                      color: "#64748b",
                      fontSize: ".8rem",
                    }}
                  >
                    No activity recorded for this period.
                  </div>
                )}
              </div>
            </section>
          </>
        )}

        {/* Footer */}
        <footer
          style={{
            fontSize: ".7rem",
            color: "#475569",
            marginTop: "2rem",
            textAlign: "center",
          }}
        >
          Solar-backed decarbonization • SunPowerScope
        </footer>
      </div>
    </main>
  );
}

export default App;
