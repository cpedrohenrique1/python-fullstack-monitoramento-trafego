package edu.redesII.monitoramentotrafego.model;

import jakarta.persistence.*;

@Entity
@Table(name = "dispositivos")
public class Dispositivo {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(unique = true, nullable = false)
    private String ip;
    @Column(nullable = false)
    private String nome;
    @Column(nullable = false)
    private double taxa;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getIp() {
        return ip;
    }

    public void setIp(String ip) {
        this.ip = ip;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getTaxa() {
        return this.taxa;
    }

    public void setTaxa(double taxa) {
        this.taxa = taxa;
    }
}
