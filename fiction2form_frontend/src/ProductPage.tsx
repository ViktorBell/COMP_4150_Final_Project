import React from 'react';
import './ProductPage.css';

const ProductPage: React.FC = () => {
    return (
        <>
            <div className={"search-bar"}><input type="text" placeholder="Search.."></input></div>
                <div className={"flex-container"}>
                    <div className={"flex-item1"}>Animals</div>
                    <div className={"flex-item2"}>Geometry</div>
                    <div className={"flex-item3"}>Vehicles</div>
                    <div className={"flex-item4"}>Characters</div>
                    <div className={"flex-item5"}>Architecture</div>
                </div>
        </>
    );
}

export default ProductPage;