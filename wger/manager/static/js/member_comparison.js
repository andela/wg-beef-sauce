let user_plot_data = JSON.parse(user_data.replace(/&quot;/g,'"'));
let user_weights = user_plot_data[0];
let dates = user_plot_data[1];
let plot_data = [];

function getRandomColor() {
 let letters = '0123456789ABCDEF';
 let color = '#';
 for (let i = 0; i < 6; i++) {
   color += letters[Math.floor(Math.random() * 16)];
 }
 return color;
}

Chart.defaults.line.spanGaps = true;

for (let user in user_weights) {
 color = getRandomColor();
 if (user_weights.hasOwnProperty(user)) {
   plot_data.push({
     label: user,
     data: user_weights[user],
     lineTension: 0.3,
     fill: false,
     backgroundColor: color,
     borderColor: color,
   })
 }
}

let chartData = {
 labels: dates,
 datasets: plot_data,
};

let chartOptions = {
 legend: {
   display: true,
   spanGaps: true,
   position: 'right',
   labels: {
     boxWidth: 15,
     fontColor: 'black'
   }
 },
 title: {
   text: 'Gym member weight comparison'
 },
 scales: {
   yAxes: [{
     scaleLabel: {
       display: true,
       labelString: 'Weight in Kg',
     },
   }],
   xAxes: [{
     scaleLabel: {
       display: true,
       labelString: 'Date',
     }
   }]
 },
};

window.onload = function () {
 let ctx = document.getElementById("chart");
 new Chart(ctx, {
 type: 'line',
 data: chartData,
 options: chartOptions
 });
};
