package edu.redesII.monitoramentotrafego.controller;

import edu.redesII.monitoramentotrafego.model.Dispositivo;
import edu.redesII.monitoramentotrafego.services.DispositivoService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

import org.springframework.http.HttpStatus;

@RestController
@RequestMapping("/dispositivos")
public class DispositivoController {
    @Autowired
    private DispositivoService dispositivoService;

    @PostMapping
    public ResponseEntity<Dispositivo> criar(@RequestBody Dispositivo dispositivo) {
        Dispositivo dispositivoCriado = dispositivoService.criarDispositivo(dispositivo);
        return ResponseEntity.status(HttpStatus.CREATED).body(dispositivoCriado);
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> buscarPorId(@PathVariable Integer id) {
        Dispositivo response = dispositivoService.buscarDispositivoPorId(id);
        return ResponseEntity.ok(response);
    }

    @GetMapping("/ip/{ip}")
    public ResponseEntity<Dispositivo> buscarPorEnderecoIp(@PathVariable String ip){
        Dispositivo dispositivo = dispositivoService.buscarDispositivoPorIp(ip);
        if (dispositivo == null){
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.ok(dispositivo);
    }

    @GetMapping
    public ResponseEntity<List<Dispositivo>> buscarTodos() {
        List<Dispositivo> dispositivoList = dispositivoService.listarTodosDispositivos();
        return ResponseEntity.ok(dispositivoList);
    }

    @PutMapping("/{id}")
    public ResponseEntity<?> atualizarDispositivoById(@PathVariable Integer id, @RequestBody Dispositivo dispositivoAtualizado) {
        Dispositivo dispositivoAtualizadoResponse = dispositivoService.atualizarDispositivoPorId(id, dispositivoAtualizado);
        return ResponseEntity.ok(dispositivoAtualizadoResponse);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteDevice(@PathVariable Integer id){
        dispositivoService.deletarDispositivo(id);
        return ResponseEntity.noContent().build();
    }

}
