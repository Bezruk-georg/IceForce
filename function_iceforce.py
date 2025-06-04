import table_data_sp
import numpy as np


# Функция интерполяции значений m, если выбрана форма треугольник
def m_triang_interpolation(table_m_triang, angle, koef_m_result):
    angle_values = np.array(table_m_triang[0])  # Значения угла табличные
    m_values = np.array(table_m_triang[1])  # Значения m табличные
    m = np.interp(float(angle), angle_values, m_values)  # Интерполяция значения
    koef_m_str = f"m = {m}"
    koef_m_result.config(text=koef_m_str)  # Вспомогательная подпись для обозначения


# Функция присваивания m при выборе прямоугольной формы и многогранника
def koef_m(event, forms, cbox_form, koef_m_result, angle):
    form_var = cbox_form.get()
    if form_var == forms[2]:  # Прямоугольник
        m = table_data_sp.m_sqad
    elif form_var == forms[1]:  # Многогранник
        m = table_data_sp.m_mnog
    elif form_var == forms[0]:  # Треугольник
        angle.config(state="normal")
        return  # Не обновляем m, пока не введён угол

    koef_m_str = f"m = {m}"
    koef_m_result.config(text=koef_m_str)
