const ctx = document.getElementById("scanChart");

if(ctx){

    new Chart(ctx, {

        type:"line",

        data:{
            labels:["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
            datasets:[{
                label:"Deepfake Detection Trend",
                data:[12,18,9,22,28,19,35],
                borderColor:"#00E5FF",
                backgroundColor:"rgba(0,229,255,0.1)",
                tension:0.4
            }]
        },

        options:{
            responsive:true,
            plugins:{
                legend:{
                    labels:{ color:"white" }
                }
            },
            scales:{
                x:{ ticks:{ color:"white" } },
                y:{ ticks:{ color:"white" } }
            }
        }

    });

}