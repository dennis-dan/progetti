import java.util.ArrayList;

public class BibliotecaTester {
    public static void main(String[] args) {
        ArrayList<Libro> books = new ArrayList<>();
        books.add(new Libro("Harry Potter", "J.K. Rowling"));
        books.add(new Libro("Il trono di spade", "George Martin"));
        books.add(new Libro("Hunger Games", "Suzanne Collins"));

        Biblioteca feltrinelliRoma = new Biblioteca(books);

        feltrinelliRoma.addBook(new Libro("Il trono di spade", "George Martin"));
        feltrinelliRoma.addBook(new Libro("Io prima di te", "Jojo Moyes"));

        feltrinelliRoma.vende("Harry Potter", "J.K. Rowling");
        feltrinelliRoma.vende("Il trono di spade", "George Martin", 8);
        feltrinelliRoma.vende("Hunger Games", "Suzanne Collins", 12);

        System.out.println("\nLIBRERIA FELTRINELLI ROMA\n");
        System.out.println("Elenco titoli disponibili:");
        System.out.println("-------------------------");

        for (Libro l : feltrinelliRoma.getLibri()) {
            System.out.println("Titolo: " + l.getTitolo());
            System.out.println("Autore: " + l.getAutore());
            System.out.println("Numero copie disponibili: " + l.getNumCopie());
            System.out.println("-------------------------");
        }

        Libro j = feltrinelliRoma.search("Io prima di te", "Jojo Moyes");
        if (j != null) {
            System.out.println(j.getTitolo() + " di " + j.getAutore() + " è presente in biblioteca!");
        } else {
            System.out.println("Purtroppo il titolo selezionato non è disponibile!");
        }
    }
}
