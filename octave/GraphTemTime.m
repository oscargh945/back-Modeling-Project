ti = [01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31]
te_minimo = [59 35 21 28 42 44 55 44 37 50 48 55 55 46 43 39 42 51 50 31 32 36 27 31 24 41 43 45 17 41 53]
te_maximo = [26 12 14 16 15 10 8 21 15 14 19 26 32 23 22 20 15 21 18 6 6 17 9 8 -1 -4 19 7 0 8 20]
te_promedio = [43 24 18 22 29 21 32 35 26 32 34 41 44 35 33 30 29 36 34 19 19 21 18 23 12 19 31 26 9 28 37]

subplot(3,1,1);
plot(tiempo,te_minimo, 'black');
title('Medicion de temperatura minima');
xlabel('Tiempo, dias');
ylabel('Temperatura, grados F');
grid on;

subplot(3,1,2);
plot(tiempo,te_maximo, 'b');
title('Medicion de temperatura maxima');
xlabel('Tiempo, dias');
ylabel('Temperatura, grados F');
grid on;

subplot(3,1,3);
plot(tiempo,te_promedio, 'g');
title('Medicion de temperatura promedio');
xlabel('Tiempo, dias');
ylabel('Temperatura, grados F');
grid on;
