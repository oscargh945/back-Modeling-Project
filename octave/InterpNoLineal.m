args = argv();

x = str2double(args{1});
X = str2num(args{2}); %#ok<ST2NM>
Y = str2num(args{3}); %#ok<ST2NM>

n = length(X);
y = 0;

for i = 1:n
  p = 1;
  for j = 1:n
    if i ~= j
      p = p * (x - X(j)) / (X(i) - X(j));
    end
  end
  y = y + p * Y(i);
end

printf("%.6f\n", y);