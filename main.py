"""Module with functions."""


def largest_sum(numbers: list[int]) -> tuple[int, int]:
    """Encontra e retorna os dois números que somados dão o maior valor."""
    if len(numbers) < 2:
        return None
    maior = max(numbers)
    numbers.remove(maior)
    segundo_maior = max(numbers)


    primeiro = min(maior, segundo_maior)  # o primeiro número da soma
    segundo = max(maior, segundo_maior)  # o segundo número da soma
    return primeiro, segundo
