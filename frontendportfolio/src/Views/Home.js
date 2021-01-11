import React, {useState, useEffect} from 'react'

function Home(){

    let screenSize='', actualMiddle='', myImg='', myParagraph='', middleStyle='', middleStyleText=''

    screenSize = useWindowSize()
    actualMiddle = screenSize.height
    myImg = document.querySelector("#image");
    myParagraph = document.querySelector("#parag");

    if (myImg){
        myImg = actualMiddle/2 - myImg.clientHeight/2
        myParagraph = actualMiddle/2 - myParagraph.clientHeight/2
    
        middleStyle = 'position: relative; top: '+myImg+'px;'
        middleStyleText = 'position: relative; top: '+myParagraph+'px; text-align: center;'
    }

    

    return (
        <div className='row justify-content-end'>
            <img id='image' Style={middleStyle} className='rounded-circle col-10 col-sm-5 p-5' src="https://pbs.twimg.com/profile_images/1257121914230845442/ROC5uHp3_400x400.jpg" alt="Daniel Uribe"/>
            <div id='parag' className="col-10 col-sm-5 p-5" Style={middleStyleText}>
                <h1 className='text-success bold text-center pt-1' >Daniel Uribe</h1>
                <p className='text-center' >
                Powder cheesecake muffin wafer caramels bear claw. Soufflé dessert toffee oat cake donut icing. Biscuit chocolate pie biscuit. Candy halvah jujubes cheesecake. Marzipan pudding macaroon soufflé tootsie roll cheesecake pudding sesame snaps. Gummies sugar plum candy canes. Sugar plum dragée halvah tiramisu carrot cake gummies donut danish. Biscuit soufflé donut ice cream chocolate cake dragée. Sweet roll pastry marshmallow topping. Jelly sweet roll sweet icing. Chocolate gingerbread candy apple pie chocolate cake bonbon donut. Candy canes cotton candy danish jujubes. Sesame snaps soufflé cupcake.
                </p>
            </div>
        </div>
    )
}

export default Home

function useWindowSize() {
    const [windowSize, setWindowSize] = useState({
        width: undefined,
        height: undefined,
    });

    useEffect(() => {
        function handleResize() {
            setWindowSize({
                width: window.innerWidth,
                height: window.innerHeight,
            });
        }

        window.addEventListener("resize", handleResize);
        handleResize();

        return () => window.removeEventListener("resize", handleResize);
    }, []);

    return windowSize;
}