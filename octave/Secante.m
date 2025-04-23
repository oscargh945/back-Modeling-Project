args = argv();
x0 = str2double(args{1});
x1 = str2double(args{2});
TOL = str2double(args{3});

sw = 1;
Cont = 1;

while sw == 1
  f1 = sin(x1) + 3*cos(x1);
  f2 = sin(x0) + 3*cos(x0);
  x2 = x1 - (x1 - x0) * (f1/(f1 - f2));
  if abs(x2-x1)<=TOL
    x = x2;
    sw = 0;
  end
  x0 = x1;
  x1 = x2;
  Cont = Cont + 1;
end

printf("ROOT=%.6f\nITER=%d\n", x, Cont);
