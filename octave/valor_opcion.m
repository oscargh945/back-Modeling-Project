arg_list = argv();
K = str2num(arg_list{1});
r = str2num(arg_list{2});
T = str2num(arg_list{3});
S0 = str2num(arg_list{4});
sigma = str2num(arg_list{5});

# Función aproximada para la CDF normal estándar (polinomio de Abramowitz y Stegun)
function p = norm_cdf_approx(x)
  a1 = 0.319381530;
  a2 = -0.356563782;
  a3 = 1.781477937;
  a4 = -1.821255978;
  a5 = 1.330274429;
  L = abs(x);
  K = 1.0 / (1.0 + 0.2316419 * L);
  w = 1.0 - 1.0 / sqrt(2*pi) * exp(-L*L/2.0) * ...
      (a1*K + a2*K^2 + a3*K^3 + a4*K^4 + a5*K^5);
  if x < 0
    p = 1.0 - w;
  else
    p = w;
  end
end

d1 = (log(S0/K) + (r + 0.5*sigma^2)*T) / (sigma*sqrt(T));
d2 = d1 - sigma*sqrt(T);
valor = S0 * norm_cdf_approx(d1) - K * exp(-r*T) * norm_cdf_approx(d2);
disp(valor);