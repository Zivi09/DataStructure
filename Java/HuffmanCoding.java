import java.util.*;

class HuffmanNode implements Comparable<HuffmanNode> {
    Character ch;
    int freq;
    HuffmanNode left, right;

    HuffmanNode(Character ch, int freq) {
        this.ch = ch;
        this.freq = freq;
        this.left = this.right = null;
    }

    @Override
    public int compareTo(HuffmanNode other) {
        return Integer.compare(this.freq, other.freq);
    }
}

public class HuffmanCoding {

    public static HuffmanNode buildHuffmanTree(Map<Character, Integer> frequency) {
        PriorityQueue<HuffmanNode> heap = new PriorityQueue<>();
        for (Map.Entry<Character, Integer> entry : frequency.entrySet()) {
            heap.add(new HuffmanNode(entry.getKey(), entry.getValue()));
        }

        while (heap.size() > 1) {
            HuffmanNode left = heap.poll();
            HuffmanNode right = heap.poll();
            HuffmanNode merged = new HuffmanNode(null, left.freq + right.freq);
            merged.left = left;
            merged.right = right;
            heap.add(merged);
        }
        return heap.poll();
    }

    public static void generateHuffmanCodes(HuffmanNode root, String currentCode, Map<Character, String> codes) {
        if (root == null) return;

        if (root.ch != null) {
            codes.put(root.ch, currentCode);
        }
        generateHuffmanCodes(root.left, currentCode + "0", codes);
        generateHuffmanCodes(root.right, currentCode + "1", codes);
    }

    public static Map<Character, Integer> calculateFrequency(String text) {
        Map<Character, Integer> frequency = new HashMap<>();
        for (char ch : text.toCharArray()) {
            frequency.put(ch, frequency.getOrDefault(ch, 0) + 1);
        }
        return frequency;
    }

    public static String huffmanEncode(String text, Map<Character, String> codes) {
        StringBuilder encodedText = new StringBuilder();
        for (char ch : text.toCharArray()) {
            encodedText.append(codes.get(ch));
        }
        return encodedText.toString();
    }

    public static String huffmanDecode(String encodedText, HuffmanNode root) {
        StringBuilder decodedText = new StringBuilder();
        HuffmanNode currentNode = root;
        for (char bit : encodedText.toCharArray()) {
            if (bit == '0') {
                currentNode = currentNode.left;
            } else {
                currentNode = currentNode.right;
            }
            if (currentNode.ch != null) {
                decodedText.append(currentNode.ch);
                currentNode = root;
            }
        }
        return decodedText.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the text to encode: ");
        String text = scanner.nextLine();

        Map<Character, Integer> frequency = calculateFrequency(text);
        HuffmanNode root = buildHuffmanTree(frequency);
        Map<Character, String> codes = new HashMap<>();
        generateHuffmanCodes(root, "", codes);

        System.out.println("\nHuffman Codes: " + codes);
        String encodedText = huffmanEncode(text, codes);
        System.out.println("Encoded Text: " + encodedText);
        String decodedText = huffmanDecode(encodedText, root);
        System.out.println("Decoded Text: " + decodedText);
        
        scanner.close();
    }
}
