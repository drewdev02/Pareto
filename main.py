import matplotlib.pyplot as plt

# Datos
causas = [
    'Vulnerabilidad a ciberataques',
    'La rápida evolución',
    'Competencia en el mercado',
    'La dependencia de proveedores',
    'La falta de diversificación',
    'Costo elevado'
]
fallos = [20, 15, 12, 10, 8, 5]

# Calcular los porcentajes y los porcentajes acumulados
porcentajes = [(fallo / sum(fallos)) * 100 for fallo in fallos]
porcentajes_acum = [sum(porcentajes[:i + 1]) for i in range(len(porcentajes))]

# Crear el gráfico de barras
fig, ax1 = plt.subplots()
ax1.bar(causas, fallos, color='b')
ax1.set_xlabel('Causas')
ax1.set_ylabel('# Fallos')
ax1.tick_params(axis='y', labelcolor='b')

# Crear el gráfico de línea
ax2 = ax1.twinx()
ax2.plot(causas, porcentajes_acum, color='r', marker='o')
ax2.set_ylabel('% Acum')
ax2.tick_params(axis='y', labelcolor='r')

# Ordenar las causas y ajustar el tamaño de la figura
fig.autofmt_xdate()

# Mostrar el diagrama de Pareto
plt.show()
