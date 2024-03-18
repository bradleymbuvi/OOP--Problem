const participants = [
    { name: "Habanero Hillary", chickenwings: 5 , hamburgers: 17, hotdogs: 11},
    { name: "Big Bob" , chickenwings: 20, hamburgers: 4, hotdogs: 11}
  ];
  
  const scoreboard = calculateScoreboard(participants);
  

function calculateScoreboard(participants) {
    // Loop through each participant
    return participants.map(participant => {
      // Calculate total score based on point system
      const score = participant.chickenwings * 5 + participant.hamburgers * 3 + participant.hotdogs * 2;
      // Return an object with name and score
      return { name: participant.name, score };
    })
    // Sort the participants by score (descending) and name (ascending)
    .sort((a, b) => b.score - a.score || (a.name > b.name ? 1 : -1));
  }



  
  console.log(scoreboard);
  
