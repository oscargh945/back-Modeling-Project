function [y] = PoliLagrange(x, X, Y)
  y=0;
  for i = 1:numel(X)
    L=1;
    for j = 1:numel(X)
      if j ~= i
        L = L * (x - X(j)) / (X(i) - X(j));
      end
    end
    y = y + L * Y(i);
  end

