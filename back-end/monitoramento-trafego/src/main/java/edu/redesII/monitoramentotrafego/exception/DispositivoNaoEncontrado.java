package edu.redesII.monitoramentotrafego.exception;

public class DispositivoNaoEncontrado extends RuntimeException {
    public DispositivoNaoEncontrado() {
        super("Dispositivo não encontrado");
    }
    public DispositivoNaoEncontrado(String message) {
        super(message);
    }
}
