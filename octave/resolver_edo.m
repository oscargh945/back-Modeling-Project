arg_list = argv();
W0 = str2num(arg_list{1});
f_expr = arg_list{2};
t0 = str2num(arg_list{3});
T = str2num(arg_list{4});
N = str2num(arg_list{5});
metodo = lower(strrep(strrep(arg_list{6}, '"', ''), "'", ''));

f_expr = strrep(f_expr, '"', '');
f_expr = strrep(f_expr, "'", '');
f_expr = strtrim(f_expr);

printf("DEBUG: f_expr='%s'\n", f_expr);

try
  f_code = strcat("@(t,W)", f_expr);
  f = eval(f_code); % usar eval directamente
  test_val = f(0, 1); % validación
catch err
  error(["Error al interpretar la función f: ", err.message]);
end

t = linspace(t0, T, N + 1);
h = (T - t0) / N;
W = zeros(1, N + 1);

if numel(W0) > 1
  W(1) = W0(1);
else
  W(1) = W0;
end

for i = 1:N
  switch metodo
    case "euler"
      Wi = W(i);
      W(i+1) = Wi + h * f(t(i), Wi);
    case "rk2"
      Wi = W(i);
      k1 = f(t(i), Wi);
      k2 = f(t(i) + h, Wi + h * k1);
      W(i+1) = Wi + h/2 * (k1 + k2);
    case "rk4"
      Wi = W(i);
      k1 = f(t(i), Wi);
      k2 = f(t(i) + h/2, Wi + h/2 * k1);
      k3 = f(t(i) + h/2, Wi + h/2 * k2);
      k4 = f(t(i) + h, Wi + h * k3);
      W(i+1) = Wi + h/6 * (k1 + 2*k2 + 2*k3 + k4);
    otherwise
      error("Método numérico no soportado.");
  end
end

disp(mat2str(t));
disp(mat2str(W));
