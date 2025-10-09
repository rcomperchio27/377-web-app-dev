function testArray() {
    
    let grades = [ 79, 80, 100, 94, 83, 92]

    $('#grades').html('Your grades are: ' + grades);

    let total = 0;
    for (let i = 0; i < grades.length; i++) {
        total += grades[i];
    }

    let average = total / grades.length;

    $('#adverage').html('Your average is: ' + average);
}

function Card(suit, rank, value) {
    this.suit = suit;
    this.rank = rank;
    this.value = value;
}


let deck = []

function shuffleDeck() {
    let suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    for (let i = 1; i < 4; i++) {
        for (let rank = 1; rank < 14; rank++) {
            console.log(rank + " of " + suits[i]);

            // seconds parameter should translate 1, 11, 12, 13 to ace, jack, queen, king respectively
            let card = new Card(suits[i], rank, rank);
            deck.push(card);
        }
    }

    // USE A READILY AVALIABLE SHUFFLE ALGORITHM (GIVE CREDIT OT THE AUTHOR) (caps)

    console.log(deck);

}

function dealCard() {
    let nextCard = deck.pop();
    $('#card').html(nextCard);
}