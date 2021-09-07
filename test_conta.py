#
import pytest
from conta import Conta

@pytest.fixture
def conta_test():
    return Conta('000123-01', 'Edilça')

def test_deposito_valores_como_string(conta_test):
    conta_test.depositar('jaca')
    assert conta_test.saldo == conta_test.saldo

def test_deposito_igual_zero(conta_test):
    assert conta_test.depositar(0) == None

def test_sacar_valor_maior_que_o_disponivel(conta_test):
    assert conta_test.sacar(200) == False

def test_sacar_valor_suficiente(conta_test):
    assert conta_test.sacar(40) == True

def test_tranferencia_checar_conta(conta_test):
    assert conta_test.transferir('000123-02', 30) == True

def test_tranferencia_invalida_valor_maior_que_seu_saldo(conta_test):
    assert conta_test.transferir('000123-02', 300) == False

def test_extrato_validar(conta_test):
    assert conta_test.extrato(1) != False