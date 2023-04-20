// List of Plant Data
const PLANTS = [{
    id: 0,
    name: "Snake Plant",
    partDes: "Sansevieria are evergreen perennials that can grow anywhere from eight inches to 12 feet high. Their sword-like leaves are approximately two feet long...",
    fullDes: "Sansevieria are evergreen perennials that can grow anywhere from eight inches to 12 feet high. Their sword-like leaves are approximately two feet long. The foliage is stiff, broad, and upright, in a dark green color variegated with white and yellow striping. They are famous for their ability to survive in the most unsuitable growing conditions. They are also renowned for their qualities that help purify the air we breathe. Since they produce oxygen mainly at night, snake plants make for a great bedroom companion.",
    maxTemp: "Max Temperature: 69",
    minTemp: "Min Temperature: 69",
    soilMois: "Suggested Soil Moisture: 100"

},
{
    id: 1,
    name: "Aloe Vera",
    partDes: "Aloe vera can grow indoors and outdoors, but if you're growing it inside, make sure to put it in a spot where it will get plenty of sunlight...",
    fullDes: "Aloe vera can grow indoors and outdoors, but if you're growing it inside, make sure to put it in a spot where it will get plenty of sunlight...South- or west-facing windows are ideal. You'll also need to water your aloe plant regularly, about once per week or when the soil is dry to the touch.",
    maxTemp: "Max Temperature: 123",
    minTemp: "Min Temperature: 321",
    soilMois: "Suggested Soil Moisture: 999"

}]

// Function to save the data of the plant 
function addToGarden() {
let data = {
    plantName: document.getElementById("plantName").innerHTML,
    minTemp: document.getElementById("minTemp").innerHTML,
    maxTemp: document.getElementById("maxTemp").innerHTML,
    soilMois: document.getElementById("soilMois").innerHTML
};
localStorage.setItem("myData", JSON.stringify(data));
}
