import { BarChart, Bar, CartesianGrid, XAxis, YAxis, Tooltip, Legend } from 'recharts';
import { withRouter } from 'react-router-dom';
import {isMobile} from 'react-device-detect';

const ChartModel = (props) => {
    const { data } = props

    if (isMobile) {
        return (
            <BarChart width={450} height={250} data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis type="number" domain={[0, 100]}/>
            <Tooltip />
            <Legend />
            <Bar dataKey="percentage" fill="#8884d8" />
            </BarChart>
    );
    } else {
        return (
             <BarChart width={500} height={250} data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis type="number" domain={[0, 100]}/>
                <Tooltip />
                <Legend />
                <Bar dataKey="percentage" fill="#8884d8" />
            </BarChart>
        );
    }
};

export default withRouter(ChartModel);
