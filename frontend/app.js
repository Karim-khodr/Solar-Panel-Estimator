async function estimate() {
  const address = document.getElementById("address").value;
  const res = await fetch(`http://localhost:8000/estimate?address=${encodeURIComponent(address)}`);
  const data = await res.json();

  document.getElementById("output").innerHTML = `
    <p><strong>Address:</strong> ${data.address}</p>
    <p><strong>Total Estimated Output:</strong> ${data.total_kwh} kWh/year</p>
    <p><strong>Avg. Irradiance:</strong> ${data.avg_irradiance.toFixed(2)} kWh/m²/day</p>
  `;
}