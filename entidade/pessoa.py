from abc import ABC, abstractmethod

class Pessoa(ABC):
  @abstractmethod
  def __init__(self, nome: str, cpf: int, senha: str):
    if isinstance(nome, str):
      self.__nome = nome
    if isinstance(cpf, int):
      self.__cpf = cpf
    if isinstance(senha, str):
      self.__senha = senha


  @property
  def nome(self):
    return self.__nome


  @nome.setter
  def nome(self, nome: str):
    self.__nome = nome


  @property
  def cpf(self):
    return self.__cpf


  @cpf.setter
  def cpf(self, cpf: int):
    self.__cpf = cpf


  @property
  def senha(self) -> str:
    return self.__senha


  @senha.setter
  def senha(self, senha: str):
    self.__senha = senha