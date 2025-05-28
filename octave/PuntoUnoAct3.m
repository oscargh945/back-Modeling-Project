TOL = 0.01;
sw = 1;
x0 = 0.1;
x1 = 0.3;
contador = 1;

while sw == 1

  f1= (3.06 - ((1-x1)*(3+x1)^0.5/x1*(x1+1)^0.5*5^0.5));
  f2= (3.06 - ((1-x0)*(3+x0)^0.5/x1*(x0+1)^0.5*5^0.5));
  x2 = x1 - (x1 - x0)*(f1/(f1 - f2));

  if abs(x2-x1) <= TOL
    x = x2;
    sw = 0;
  end
  x0 = x1;
  x1 = x2;
  contador= contador+1;
end
#af = x
x
contador
