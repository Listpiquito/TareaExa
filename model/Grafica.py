
plt.figure(figsize=(8,6))  # tamaño opcional
        plt.plot(Qo,Pwf, marker='o', color='b', linewidth=2)

        # Etiquetas y título
        plt.title("Curva IPR - Yacimiento saturado", fontsize=14)
        plt.ylabel("Presión de fondo fluyente Pwf (psi)", fontsize=12)
        plt.xlabel("Tasa de producción Q (bbl/día)", fontsize=12)
        # Cuadrícula y visualización
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()