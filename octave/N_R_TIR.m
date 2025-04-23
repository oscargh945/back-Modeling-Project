args = argv();
x1 = str2double(args{1});  % valor inicial r
TOL = str2double(args{2});
inversion = str2double(args{3});
flujos = str2num(args{4}); %#ok<ST2NM>

sw = 1;
Cont = 1;

while sw == 1
  f = inversion;
  Df = 0;
  for t = 1:length(flujos)
    f += flujos(t) / (1 + x1)^t;
    Df += -t * flujos(t) / (1 + x1)^(t + 1);
  end

  x2 = x1 - (f / Df);
  if abs(x2 - x1) <= TOL
    x = x2;
    sw = 0;
  end

  x1 = x2;
  Cont = Cont + 1;
end

printf("ROOT=%.6f\nITER=%d\n", x, Cont);
