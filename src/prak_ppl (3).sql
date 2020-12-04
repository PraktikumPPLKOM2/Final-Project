-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 30 Nov 2020 pada 02.25
-- Versi server: 10.1.38-MariaDB
-- Versi PHP: 7.3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `prak_ppl`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `alert`
--

CREATE TABLE `alert` (
  `id` int(11) NOT NULL,
  `idmurid` int(11) NOT NULL,
  `idortu` int(11) NOT NULL,
  `pesan` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `alert`
--

INSERT INTO `alert` (`id`, `idmurid`, `idortu`, `pesan`) VALUES
(1, 18, 15, 'KERJAKAN TUGASNYA YANG BENER');

-- --------------------------------------------------------

--
-- Struktur dari tabel `kelas`
--

CREATE TABLE `kelas` (
  `id` int(11) NOT NULL,
  `namakelas` varchar(255) NOT NULL,
  `enrollmentkey` varchar(255) NOT NULL,
  `idtugas` varchar(255) DEFAULT NULL,
  `idmember` varchar(255) DEFAULT NULL,
  `idteacher` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `kelas`
--

INSERT INTO `kelas` (`id`, `namakelas`, `enrollmentkey`, `idtugas`, `idmember`, `idteacher`) VALUES
(1, 'percobaan', '123', '', '18', '16'),
(2, 'matematika statistika', '123', '', '18', '16'),
(3, 'biologi', '123', '43,44', '18,23', '16'),
(4, 'ppl', '123', '45', '18,23', '16');

-- --------------------------------------------------------

--
-- Struktur dari tabel `nilai`
--

CREATE TABLE `nilai` (
  `id` int(11) NOT NULL,
  `idmurid` int(11) DEFAULT NULL,
  `idtugas` int(11) DEFAULT NULL,
  `nilai` int(11) DEFAULT NULL,
  `submission` tinyint(1) NOT NULL,
  `file` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `nilai`
--

INSERT INTO `nilai` (`id`, `idmurid`, `idtugas`, `nilai`, `submission`, `file`) VALUES
(4, 18, 44, 0, 0, 'file1'),
(5, 23, 44, 0, 0, ''),
(6, 18, 45, 100, 1, 'file');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tugas`
--

CREATE TABLE `tugas` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `deskripsi` varchar(255) DEFAULT NULL,
  `idkelas` int(11) DEFAULT NULL,
  `deadline` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `tugas`
--

INSERT INTO `tugas` (`id`, `nama`, `deskripsi`, `idkelas`, `deadline`) VALUES
(43, 'Sistem Pernafasan', 'Buatlah gambar sistem pernafasan', 3, '2020-12-15 15:30:00'),
(44, 'lololol', 'ololol', 3, '2020-12-18 15:30:00'),
(45, 'ERD', 'gambar ERD project anda', 4, '2020-12-04 15:45:00');

-- --------------------------------------------------------

--
-- Struktur dari tabel `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `status` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `notelp` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `alamat` varchar(255) NOT NULL,
  `idkelas` varchar(255) DEFAULT NULL,
  `idtugas` varchar(255) DEFAULT NULL,
  `idmuridnyaortu` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `users`
--

INSERT INTO `users` (`id`, `status`, `username`, `password`, `nama`, `notelp`, `email`, `alamat`, `idkelas`, `idtugas`, `idmuridnyaortu`) VALUES
(9, 'Guru', 'yohantidakganteng', 'yohan321', 'Yohan', '0868969696969', 'yohan@gmail.com', 'jalan raya', '', NULL, NULL),
(15, 'Orang Tua', 'donitan', 'doni123', 'doni tan', '08521346487122', 'doni.tan55@gmail.com', 'jalan karya', '', NULL, '18,23'),
(16, 'Guru', 'klee', 'klee123', 'klee oneechan', '08124548949', 'klee@gmail.com', 'jalanan', '1', NULL, NULL),
(17, 'Guru', 'barbatos', 'barbatos123', 'barbatos', '08', 'barbatos@gmail.com', 'jalanan', '', NULL, NULL),
(18, 'Murid', 'zhongli', 'zhongli123', 'zhongli', '08', 'zhongli@gmail.com', 'jalan geo', '1,2,3,4', NULL, NULL),
(19, 'Guru', 'bebas', 'bebas123', 'bebas', '08', 'bebas@gmail.com', 'bebas', '', NULL, NULL),
(20, 'Murid', 'kurama', 'kurama123', 'kurama', '08', 'kurama@gmail.com', 'jalan', '', NULL, NULL),
(21, 'Orang Tua', 'tartaglia', 'tartaglia123', 'tartaglia', '08', 'tartaglia@gmail.com', 'jalan', '', NULL, NULL),
(22, 'Murid', 'yakmeng', 'yakmeng123', 'yakmeng', '08', 'yakmeng@gmail.com', 'jalan', '', NULL, NULL),
(23, 'Murid', 'senpai', 'senpai', 'senpai', '08', 'senpai@', 'jalan', '3,4', NULL, NULL),
(24, 'Murid', 'kirana', 'kirana', 'kirana', '08', 'kirana@', 'jalan', '', NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `alert`
--
ALTER TABLE `alert`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `kelas`
--
ALTER TABLE `kelas`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `nilai`
--
ALTER TABLE `nilai`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idmurid` (`idmurid`),
  ADD KEY `idtugas` (`idtugas`);

--
-- Indeks untuk tabel `tugas`
--
ALTER TABLE `tugas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idkelas` (`idkelas`);

--
-- Indeks untuk tabel `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `alert`
--
ALTER TABLE `alert`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `kelas`
--
ALTER TABLE `kelas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `nilai`
--
ALTER TABLE `nilai`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `tugas`
--
ALTER TABLE `tugas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT untuk tabel `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `nilai`
--
ALTER TABLE `nilai`
  ADD CONSTRAINT `nilai_ibfk_1` FOREIGN KEY (`idmurid`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `nilai_ibfk_2` FOREIGN KEY (`idtugas`) REFERENCES `tugas` (`id`);

--
-- Ketidakleluasaan untuk tabel `tugas`
--
ALTER TABLE `tugas`
  ADD CONSTRAINT `tugas_ibfk_1` FOREIGN KEY (`idkelas`) REFERENCES `kelas` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
