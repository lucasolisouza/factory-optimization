# Production Optimization with Linear Programming / Otimização de Produção com Programação Linear

## Project Description / Descrição do Projeto

This project demonstrates the application of Linear Programming to optimize production processes in a small factory that manufactures two products. The goal is to determine the optimal production quantities to maximize profit while respecting resource constraints.

Este projeto demonstra a aplicação de Programação Linear para otimizar processos de produção em uma fábrica que produz dois produtos. O objetivo é determinar as quantidades ótimas de produção para maximizar o lucro, respeitando as restrições de recursos.

## Problem Definition / Definição do Problema

### Products / Produtos
| Product | Profit | Machine Hours | Raw Material |
|---------|--------|---------------|--------------|
| A       | R$ 40  | 2 hours       | 3 kg         |
| B       | R$ 30  | 1 hour        | 2 kg         |

### Constraints / Restrições
- **Machine hours**: 100 hours available / 100 horas disponíveis
- **Raw material**: 120 kg available / 120 kg disponíveis

## Mathematical Model / Modelo Matemático

### Decision Variables / Variáveis de Decisão
- \( x \) = Quantity of Product A / Quantidade do Produto A
- \( y \) = Quantity of Product B / Quantidade do Produto B

### Objective Function / Função Objetivo
max Z = 40x + 30y

### Constraints / Restrições
- 2x + y ≤ 100 (Machine hours/Horas de máquina)
- 3x + 2y ≤ 120 (Raw material/Matéria-prima)
- x ≥ 0, y ≥ 0 (Non-negativity/Não-negatividade)

## Optimal Solution / Solução Ótima
- **Product A / Produto A**: 0 units / unidades
- **Product B / Produto B**: 60 units / unidades  
- **Maximum Profit / Lucro Máximo**: R$ 1,800

## Implementation / Implementação

### Technologies Used / Tecnologias Utilizadas
- **Python 3.8+**
- **PuLP**: Linear Programming library / Biblioteca de Programação Linear
- **Streamlit**: Web application framework / Framework para aplicações web

### Installation / Instalação
```bash
git clone https://github.com/lucasolisouza/factory-optimization.git
cd factory-optimization
pip install -r requirements.txt
```

### Execution / Execução
```bash
streamlit run app.py


