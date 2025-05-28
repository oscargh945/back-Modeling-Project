function [I] = Integral(IO, X, Y)
  I(1) = IO;
  N = numel(X)
  for n = 2:N
    I(n) = I(n-1) + 0.5*(X(n) - X(n-1)) * (Y(n) + Y(n-1));
  end
plot(X, I, 'k-');

