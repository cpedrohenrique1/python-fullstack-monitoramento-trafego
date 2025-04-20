package edu.redesII.monitoramentotrafego.repository;

import edu.redesII.monitoramentotrafego.model.Dispositivo;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface DispositivoRepository extends JpaRepository<Dispositivo, Integer> {

    @Query(value = "SELECT * FROM dispositivos WHERE ip = :ip;", nativeQuery = true)
    Optional<Dispositivo> findDispositivoByIp(@Param("ip") String ip);
}
