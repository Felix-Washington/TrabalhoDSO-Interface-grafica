from abc import ABC, abstractmethod
import os


class AbstractControlador(ABC):

  @abstractmethod
  def __init__(self):
    pass


  @abstractmethod
  def abre_tela_inicial(self):
    pass

  @abstractmethod
  def adiciona(self):
    pass


  @abstractmethod
  def remove(self,dados):
    pass


  @abstractmethod
  def atualiza(self,dados_obj):
    pass


  def lista(self):
    pass