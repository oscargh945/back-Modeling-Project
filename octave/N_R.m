args = argv();
x1 = str2double(args{1});
TOL = str2double(args{2});

sw = 1;
Cont = 1;

while sw == 1
  f = 3*x1^3 - 2*x1 + 8;
  Df = 9*x1^2 - 2;
  x2 = x1 - (f/Df);
  if abs(x2-x1)<=TOL
    x = x2;
    sw = 0;
  end
  x1 = x2;
  Cont = Cont + 1;
end

printf("ROOT=%.6f\nITER=%d\n", x, Cont);
