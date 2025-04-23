args = argv();
x1 = str2double(args{1});
KIC = str2double(args{2});
w = str2double(args{3});
Sigma = str2double(args{4});
TOL = str2double(args{5});

sw = 1;
Cont = 1;

while sw == 1
  Y = (1.99 - 0.4 * (x1/w) + 18.7 * (x1/w)^2 - 38.48 * (x1/w)^3 + 53.85 * (x1/w)^4);
  x2 = (KIC/(Sigma * Y))^2;
  if abs(x2-x1)<=TOL
    x = x2;
    sw = 0;
  end
  x1 = x2;
  Cont = Cont + 1;
end

printf("ROOT=%.6f\nITER=%d\n", x, Cont);
