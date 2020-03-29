function myBmi() {
    var a,g,w,h,bmi_result,bmi_child;
    a = document.getElementById("form1");
    g = a.elements["age"].value;
    h = parseFloat(a.elements["height"].value);
    w = parseFloat(a.elements["weight"].value);

    bmi_result = w / (h**2) ;
    bmi_child = w / (h**2) * 703;

     


    
    if (g == 'adult'){
        document.getElementById("demo1").innerHTML="Your BMI is: " +bmi_result;
        if (bmi_result < 18.5 ) {
            document.getElementById("demo").innerHTML="Underweight";
        }

        else if(bmi_result >= 18.5 && bmi_result <=24.9 ) {
            document.getElementById("demo").innerHTML="Normal Weight";
        }

        else if(bmi_result >= 25 && bmi_result <=29.9 ){
            document.getElementById("demo").innerHTML="Over Weight";
        }

        else {
            document.getElementById("demo").innerHTML="Obessed";

        }

    }

    else{
        document.getElementById("demo1").innerHTML="Your BMI is: " +bmi_child +" percentile";
        if (bmi_child < 5 ){
            document.getElementById("demo").innerHTML="Underweight";
        }

        else if(bmi_result >= 5 && bmi_result < 85 ){
            document.getElementById("demo").innerHTML="Normal Weight";
        }

        else if(bmi_result >= 85 && bmi_result < 95 ){
            document.getElementById("demo").innerHTML="Over Weight";
        }

        else {
            document.getElementById("demo").innerHTML="Obese";

        }
    }
}
     


    











