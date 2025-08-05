//La biblioteca è una raccolta di libri e offre alcune funzionalità: aggiungere un libro (se gia presente aumentare numero copie di 1 unita)
//aggiungere delle copie, ricercare un libro dal titolo e dall'autore, se è presente restituisci libro, altrimenti null
//un metodo vende che presi in input titolo e autore; un metodo vende che prende in input titolo autore e quantità. 
//stampa numero richiesto non disponibile e vendi quantità massima
import java.util.ArrayList;

public class Biblioteca {
    private ArrayList<Libro> libri;

    public Biblioteca(ArrayList<Libro> libri) {
        this.libri = libri;
    }

    public void addBook(Libro nuovoLibro) {
        for (Libro l : libri) {
            if (l.getTitolo().equalsIgnoreCase(nuovoLibro.getTitolo()) &&
                l.getAutore().equalsIgnoreCase(nuovoLibro.getAutore())) {
                l.incrementaCopie(1);
                return;
            }
        }
        libri.add(nuovoLibro);
    }

    public void vende(String titolo, String autore) {
        vende(titolo, autore, 1);
    }

    public void vende(String titolo, String autore, int quantita) {
        for (Libro l : libri) {
            if (l.getTitolo().equalsIgnoreCase(titolo) &&
                l.getAutore().equalsIgnoreCase(autore)) {
                if (l.decrementaCopie(quantita)) {
                    System.out.println("Vendute " + quantita + " copie di: " + titolo);
                } else {
                    System.out.println("Non ci sono abbastanza copie di: " + titolo);
                }
                return;
            }
        }
        System.out.println("Libro non trovato: " + titolo);
    }

    public Libro search(String titolo, String autore) {
        for (Libro l : libri) {
            if (l.getTitolo().equalsIgnoreCase(titolo) &&
                l.getAutore().equalsIgnoreCase(autore)) {
                return l;
            }
        }
        return null;
    }

    public void removeBook(String titolo, String autore) {
        for (int i = 0; i < libri.size(); i++) {
            Libro l = libri.get(i);
            if (l.getTitolo().equalsIgnoreCase(titolo) &&
                l.getAutore().equalsIgnoreCase(autore)) {
                libri.remove(i);
                System.out.println("Libro rimosso: " + titolo);
                return;
            }
        }
        System.out.println("Libro da rimuovere non trovato: " + titolo);
    }

    public ArrayList<Libro> getLibri() {
        return libri;
    }
}
