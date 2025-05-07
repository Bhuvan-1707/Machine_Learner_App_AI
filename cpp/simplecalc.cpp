#include <pybind11/pybind11.h>
#include <cmath>

namespace py = pybind11;

// Adding two numbers definition
double add(double a, double b) {
    return a + b;
}
// Subtracting two numbers definition
double subtract(double a,double b){
    return a - b;
}
// Multiply two numbers definition
double multiply(double a,double b){
    return a * b;
}
// Dividing two numbers definition
double divide(double a,double b){
    return a / b;
}
// Exponenting a number to the power of another definition
double exponent(double a){
    double iter=1.0;
    double nt=1,ntold=1;
    double sum;
    sum = ntold;
    if(a>=0){
        while(nt>0.000000000001){
            nt = ntold*(a/iter);
            sum+=nt;
            ntold=nt;
            iter+=1;
        }
        return sum;
    }
    else{
        while(nt>0.000000000001){
            nt = ntold*(-a/iter);
            sum+=nt;
            ntold=nt;
            iter+=1;
            }
        return 1/sum;
    }
}

double logarithm(double a){
    return cmath.log(a);
    }

PYBIND11_MODULE(simplecalc, m) {
    m.doc() = "Pybind11 module for simple calculator";
    m.def("add", &add, "A function that adds two numbers");
    m.def("subtract", &subtract, "A function that subtracts two numbers");
    m.def("multiply", &multiply, "A function that multiplies two numbers");
    m.def("divide", &divide, "A function that divides two numbers");
    m.def("exponent", &exponent, "A function that exponents a number to the power of another");
    m.def("logarithm", &logarithm, "A function that logarithms a number to the base of another");
}
