def generar_diagnostico(datos):
    """
    Генерация гипотезы на основе данных осмотра.
    """
    hipotesis = []

    # Пример логики для генерации гипотез
    if datos.get('dolor') == 'Сильная' and datos.get('otek') == 'Сильный':
        hipotesis.append("Сильная боль и выраженный отек указывают на воспаление или травму.")

    if datos.get('movilidad') == 'Ограниченная' and datos.get('krepitaciya') == 'Присутствует':
        hipotesis.append("Ограничение движений и крепитация могут быть признаком артроза.")

    if datos.get('ugol_norberg') == '<90°':
        hipotesis.append("Угол Норберга менее 90° подтверждает дисплазию тазобедренного сустава.")

    if not hipotesis:
        hipotesis.append("Патологий не выявлено.")
    
    return hipotesis
