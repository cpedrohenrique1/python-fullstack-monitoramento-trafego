package edu.redesII.monitoramentotrafego.services;

import edu.redesII.monitoramentotrafego.exception.DispositivoNaoEncontrado;
import edu.redesII.monitoramentotrafego.model.Dispositivo;
import edu.redesII.monitoramentotrafego.repository.DispositivoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class DispositivoService {

    @Autowired
    private DispositivoRepository dispositivoRepository;

    public Dispositivo criarDispositivo(Dispositivo dispositivo) {
        return dispositivoRepository.save(dispositivo);
    }

    public Dispositivo buscarDispositivoPorId(Integer id) {
        return dispositivoRepository.findById(id).orElseThrow(() -> new DispositivoNaoEncontrado("Dispositivo com " + id + " não encontrado"));
    }

    public Dispositivo buscarDispositivoPorIp(String ip) {
        return dispositivoRepository.findDispositivoByIp(ip).orElseThrow(() -> new DispositivoNaoEncontrado("Dispositivo com " + ip + " não encontrado"));
    }

    public List<Dispositivo> listarTodosDispositivos() {
        return dispositivoRepository.findAll();
    }

    public Dispositivo atualizarDispositivoPorId(Integer id, Dispositivo dispositivoAtualizado) {
        if (!this.dispositivoRepository.existsById(id)){
            throw new DispositivoNaoEncontrado();
        }
        Dispositivo dispositivoExistente = this.buscarDispositivoPorId(id);
        dispositivoExistente.setIp(dispositivoAtualizado.getIp());
        dispositivoExistente.setNome(dispositivoAtualizado.getNome());
        dispositivoExistente.setTaxa(dispositivoAtualizado.getTaxa());
        return this.criarDispositivo(dispositivoExistente);
    }

    public void deletarDispositivo(Integer id) {
        if (!this.dispositivoRepository.existsById(id)) {
            throw new DispositivoNaoEncontrado("Dispositivo com " + id + " não encontrado");
        }
        dispositivoRepository.deleteById(id);
    }
}
