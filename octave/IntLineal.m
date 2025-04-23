%function IntLineal()
args = argv();
x = str2double(args{1});
X = str2num(args{2});
Y = str2num(args{3});

for i = 1:numel(X) - 1
    if x >= X(i) && x <= X(i+1)
      y = (Y(i + 1) - Y(i)) / (X(i+1) - X(i)) * (x - X(i)) + Y(i);
      printf("%.6f\n", y);
      return
    end
end
